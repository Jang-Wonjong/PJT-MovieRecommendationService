<template>
  <div>
    <h1>DETAIL</h1>
    <div v-if="SelectedMovie">
      <img :src="imgSrc" alt="">
    </div>
    <span>{{ SelectedMovie }}</span>
    <div>
      <input 
        type="text"
        v-model.trim="content"
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
              v-model.trim="contentUpdate"
              @keyup.enter="updateReview(review)"
            >
            <button @click="updateReview(review)">저장</button>
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
      content: null,
      contentUpdate: null,
      isReviewUpdate: false,
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
        content: this.content,
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
      this.content = null
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
        content: this.contentUpdate,
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}/review/${review.id}/`,
        data: reviewItem,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          // this.reviews += res.data
          this.getReviews()
        })
        .catch(err => {
          console.log(err)
        })
      this.contentUpdate = null
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