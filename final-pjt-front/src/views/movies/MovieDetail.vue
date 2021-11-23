<template>
    <div class="container contain" v-if="SelectedMovie">
      <div 
      class="movie-detail-image"
      :style="`background-image:url('https://image.tmdb.org/t/p/original${SelectedMovie.backdrop_path}');`"
      >
      </div>
      <div class="movie-content d-flex">
        <img class="mt-2" :src="imgSrc" alt="" style="height: 80vh;">
        <div class="ml-4 w-75">
          <h1 class="h1Tag">{{ SelectedMovie.title }}</h1>
          <div class="movie-information mt-3">
            <span class="spanTag mt-3">{{ SelectedMovie }}</span>
          </div>
          <p>{{this.$store.state.id}}</p>
        </div>
        <!-- My movie -->
        <div class="outerDivFull" >
          <div class="switchToggle">
              <input type="checkbox" 
                id="switch"
                v-model="isUserMovie"
                @click="userMovie"
              >
              <label for="switch"></label>
          </div>
        </div>
      </div>

      <review class="movie-content"></review>
      <div class="community-reviewTag">
        <input 
          type="text"
          v-model.trim="reviewContent"
          @keyup.enter="createReview"
        >
        <button @click="createReview">리뷰 작성</button><br>
      </div>
      <div class="community-content">
        <ul>
          <li v-for="review in reviews" :key="review.id">
            <span @click="moveToProfile(review.user_id)">정보: {{ review.user_id }}</span><br>
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
import { mapGetters } from 'vuex'
import Review from '@/components/Review.vue'


export default {
  name: 'MovieDetail',
  components: {
    Review
  },
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

      isUserMovie: false,
    }
  },
  methods: {
     // 포스터 배경 백드롭 이미지 불러오는 함수
    image(img) {
      console.log();
      return `https://image.tmdb.org/t/p/original/${img}`;
    },
    // movie
    getMovie: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}`,
        headers: this.config
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
        headers: this.config
      })
        .then(res => {
          console.log(res)
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
        headers: this.config
      })
        .then(res => {
          console.log(res)
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
        headers: this.config
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
        headers: this.config
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
        headers: this.config
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
      // console.log(review.id)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movie/review/${review.id}/comment/`,
        data: commentItem,
        headers: this.config
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
        headers: this.config
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
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.getComments(review)
        })
        .catch(err => {
          console.log(err)
        })
      this.commentContentUpdate = null
    },
    userMovie: function () {
      if (this.isUserMovie) {
        this.userMovieRemove()
      } else {
        this.userMovieAdd()
      }
    },
    userMovieAdd: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}/user-movies/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.isUserMovie = true
          // this.getMovie()
        })
        .catch(err => {
          console.log(err)
        })
    },
    userMovieRemove: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movie/${this.SelectedMovieId}/user-movies/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.isUserMovie = false
          // this.getMovie()
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToProfile: function (userId) {
      this.$router.push({
        name: 'UserProfile',
        query: { userId }  
      })
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
    ...mapGetters([
      'config',
    ]),
    imgSrc: function () {
      return 'https://image.tmdb.org/t/p/w400' + this.SelectedMovie.poster_path
    },
  },
}
</script>

<style scoped>
.contain {
  position: relative;
  padding: 40px 40px;
}

.movie-content {
  position: relative;
  border: white;
  z-index: 999;
}
  
.is-completed {
  text-decoration: line-through;
  color: rgb(112, 112, 112);
}

/* 영화 제목 폰트 수정 */
.h1Tag {
  font-family: 'Noto Sans KR', sans-serif;
}

/* 영화 정보 폰트랑 위치 */
.spanTag {
  font-family: 'Noto Sans KR', sans-serif;
  text-align: left;
}

/* 리뷰 폰트 */
.reviewTag {
  font-family: 'Noto Sans KR', sans-serif;
}

/* 댓글 폰트 */
.commentTag {
  font-family: 'Sunflower', sans-serif;
}

/* 포스터 백그라운드 이미지 설정 */
.movie-detail-image {
  background-size: cover;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

/* 포스터 백그라운드 이미지 설정 */
.movie-detail-image::after {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  min-height: 100vh;
  background-color: rgb(40, 40, 40);
  opacity: 0.7;
  content: "";
  display: block;
}

/* 영화 디테일 구역 */
.movie-information {
  max-width: 80%;
  font-size: 14px;
  color: #dddddddd;
  margin: auto;
}


/* 영화 디테일 구역 */
.h1Tag {
  margin-left: 5px;
  color: #fff;
}

/* 리뷰 구역 */
.community-content {
  position: relative;
  z-index: 99;
  color: #fff;
}

/* 댓글 구역 */
.community-reviewTag {
  position: relative;
    z-index: 99;
    color: #fff;
}

</style>