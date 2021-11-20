<template>
  <div>
    <h1>DETAIL</h1>
    <div v-if="SelectedMovie">
      <img :src="imgSrc" alt="">
    </div>
    <span>{{ SelectedMovie }}</span>
    <button>my list</button>  <!-- 내 영화 -->
    <div>
      <input 
        type="text"
        v-model.trim="reviewContent"
        @keyup.enter="createReview"
      >
      <button @click="createReview">리뷰 작성</button><br>
    </div>
    <div>
      <ul>
        <li v-for="review in reviews" :key="review.id">
          <span>리뷰: {{ review.content }}</span><br>
          <span>평점: {{ review.rank }}</span><br>
          <button @click="isReviewUpdate=true">수정</button>
          <button @click="deleteReview(review)">삭제</button>
          <div v-if="isReviewUpdate">
            <input 
              type="text"
              v-model.trim="reviewContentUpdate"
              @keyup.enter="updateReview(review)"
            >
            <button @click="updateReview(review)">저장</button>
          </div>
          
          <button @click="getComments(review)">댓글 보기</button>
          <div>
            <input 
              type="text"
              v-model.trim="commentContent"
              @keyup.enter="createComment(review)"
            >
            <button @click="createComment(review)">댓글 생성</button>
            <li v-for="comment in comments" :key="comment.id">
              <span>댓글: {{ comment }}</span><br>
              <input 
                type="text"
                v-model.trim="commentContentUpdate"
                @keyup.enter="updateComment(review, comment)"
              >
              <button @click="updateComment(review, comment)">수정</button>
              <button @click="deleteComment(review, comment)">삭제</button>
            </li>
          </div>
          <hr>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      SelectedMovie: null,
      SelectedMovieId: null,  // MovieList에서 query로 넘겨준 movie id 받는 변수

      reviews: null,
      reviewContent: null,
      reviewContentUpdate: null,
      isReviewUpdate: false,

      comments: null,
      commentContent: null,
      commentContentUpdate: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    // movie
    getMovie: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.SelectedMovie = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    // review
    getReviews: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}/review/`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.reviews = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createReview: function () {
      const reviewItem = {
        content: this.reviewContent,
        rank: 5,
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}/review/`,
        data: reviewItem,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.reviews += res.data
          this.getReviews()
        })
        .catch(err => {
          console.log(err)
        })
      this.reviewContent = null
    },
    deleteReview: function (review) {
      // console.log(review)
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}/review/${review.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.getReviews()
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview: function (review) {
      const reviewItem = {
        ...review,
        content: this.reviewContentUpdate,
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}/review/${review.id}/`,
        data: reviewItem,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.getReviews()
        })
        .catch(err => {
          console.log(err)
        })
      this.reviewContentUpdate = null
    },
    // comment
    getComments: function (review) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movie/review/${review.id}/comment/`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.comments = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createComment: function (review) {
      const commentItem = {
        content: this.commentContent,
      }
      console.log(review.id)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movie/review/${review.id}/comment/`,
        data: commentItem,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.comments += res.data
          this.getComments(review)
        })
        .catch(err => {
          console.log(err)
        })
      this.commentContent = null
    },
    deleteComment: function (review, comment) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movie/review/${review.id}/comment/${comment.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.getComments(review)
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateComment: function (review, comment) {
      const commentItem = {
        ...comment,
        content: this.commentContentUpdate,
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movie/review/${review.id}/comment/${comment.id}/`,
        data: commentItem,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.getComments(review)
        })
        .catch(err => {
          console.log(err)
        })
      this.commentContentUpdate = null
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.SelectedMovieId = this.$route.query.movieId
      this.getMovie()
      this.getReviews()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
  computed: {
    imgSrc: function () {
      return 'https://image.tmdb.org/t/p/w400' + this.SelectedMovie.poster_path
    }
  }
}
</script>

<style scoped>
  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>