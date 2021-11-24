<template>
  <div class="container contain" v-if="SelectedMovie">
    <div 
    class="movie-detail-image"
    :style="`background-image:url('https://image.tmdb.org/t/p/original${SelectedMovie.backdrop_path}');`"
    >
    </div>
    <div class="movie-content d-flex">
      <img :src="imgSrc" alt="" style="height: 80vh;">
      <div class="movie-info ml-4 w-75">
        <h1 class="h1Tag">{{ SelectedMovie.title }}</h1>
        <div class="movie-information mt-3">
          <p class="spanTag1 mt-3">{{ SelectedMovie.original_title }}</p><br>
          <p class="spanTag mt-3">{{ SelectedMovie.overview }}</p><br>
          <p class="spanTag mt-3">개봉일 : {{ SelectedMovie.release_date }}</p>
          <p class="spanTag mt-3">평점 : {{ SelectedMovie.vote_average }}</p><br>
        </div>
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

    <!-- 리뷰 -->
    <div class="justify-content-center mt-5 border-left border-right review-body">
      <div class="d-flex justify-content-center pt-3 pb-2">
        <input type="text" name="text" placeholder="add review" class="form-control addtxt"
        v-model.trim="reviewContent"
        @keyup.enter="createReview">
      </div>
        <div class="d-flex justify-content-center py-2" v-for="review in reviews" :key="review.id">
          <div class="second py-2 px-2" >
            <span class="text1">{{ review.content }}</span>
            <div class="d-flex justify-content-between py-1 pt-2">
              <span class="text2" @click="moveToProfile(review.user_id)">user : {{ review.user_id }}</span><br>
              <div class="d-flex"> 
                <span class="text3" >평점 : {{ review.rank }}점</span><br>
              </div>
            </div>
                <div>
                <button class="btn btn-outline-warning m-1" @click="review.isReviewUpdate=true"><i class="fas fa-eraser"></i></button>
                <button class="btn btn-outline-warning m-1" @click="deleteReview(review)"><i class="fas fa-trash-alt"></i></button>
                <button class="btn btn-outline-info m-1" @click="getComments(review)" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample"><i class="far fa-comment-dots"></i></button>
                <div v-if="review.isReviewUpdate">
                  <input 
                    type="text"
                    v-model.trim="reviewContentUpdate"
                    @keyup.enter="updateReview(review)"
                    class="form-control reviewupdate_addtxt"
                    placeholder="입력하고 enter"
                  >
                </div>
                </div> 
        <!-- 댓글댓글 -->
        <div class="collapse" id="collapseExample">
          <div class="comment_card card-body second2">
            <input 
              type="text"
              v-model.trim="commentContent"
              @keyup.enter="createComment(review)"
              class="form-control comment_addtxt"
              placeholder="add comment"
            >
            <div v-for="comment in comments" :key="comment.id">
              <span>user {{ comment.id }} : {{ comment.content }}</span>
              <button class="btn btn-outline-warning m-1" @click="comment.isCommentUpdate=true"><i class="fas fa-eraser"></i></button>
              <button class="btn btn-outline-warning m-1" @click="deleteComment(review, comment)"><i class="fas fa-trash-alt"></i></button>
              <div v-if="comment.isCommentUpdate">
              <input 
                class="form-control commentupdate_addtxt"
                type="text"
                v-model.trim="commentContentUpdate"
                @keyup.enter="updateComment(review, comment)"
                placeholder="입력하고 enter"
              >
              </div>
            </div>
          </div>
        </div>
        <!-- 댓글댓글 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'


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
      isCommentUpdate:false,

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
          this.reviews = res.data.map(review => {
            return {
              ...review,
              isReviewUpdate: false
            }
          })
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
          this.isReviewUpdate=false
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
          this.comments = res.data.map(comment => {
            return {
              ...comment,
              isCommentUpdate: false
            }
          })
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
          this.isCommentUpdate=false
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
  /* background-color: black; */
  /* opacity: 0.3; */
}

.movie-info {
  /* position: fixed; */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  min-height: 100%;
  background-color: rgb(40, 40, 40);
  opacity: 0.6;
  content: "";
  display: block;
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
  font-size: 15px;
}

.spanTag1 {
  font-family: 'Noto Sans KR', sans-serif;
  text-align: left;
  font-size: 30px;
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
  font-size: 18px;
  color: #fff;
  margin: auto;
  /* z-index: 999; */
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



/* my movie add */
.outerDivFull { 
  margin:50px; 
} 

.switchToggle input[type=checkbox] {
  height: 0; width: 0; visibility: hidden; position: absolute; 
}

.switchToggle label {cursor: pointer; text-indent: -9999px; width: 70px; max-width: 70px; height: 30px; background: #212529; display: block; border-radius: 100px; position: relative; }
.switchToggle label:after {content: ''; position: absolute; top: 2px; left: 2px; width: 26px; height: 26px; background: #dddddd; border-radius: 90px; transition: 0.3s; }
.switchToggle input:checked + label, .switchToggle input:checked + input + label  {background: #e4007f; }
.switchToggle input + label:before, .switchToggle input + input + label:before {content: ''; position: absolute; top: 5px; left: 35px; width: 26px; height: 26px; border-radius: 90px; transition: 0.3s; text-indent: 0; color:#dddddd; }
.switchToggle input:checked + label:before, .switchToggle input:checked + input + label:before {content: ''; position: absolute; top: 5px; left: 10px; width: 26px; height: 26px; border-radius: 90px; transition: 0.3s; text-indent: 0; color: #dddddd; }
.switchToggle input:checked + label:after, .switchToggle input:checked + input + label:after {left: calc(100% - 2px); transform: translateX(-100%); }
.switchToggle label:active:after {width: 60px; } 
.toggle-switchArea { margin: 10px 0 10px 0; }



/* 리뷰 */
.review-body {
  background-color: rgba(255, 255, 255, 0.493);
  position: relative;
  z-index: 99;
}

.addtxt {
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
  font-size: 13px;
  width: 70%;
  background-color: #dddddd;
  font-weight: 500;
  font-family: 'Sunflower', sans-serif;
}

.form-control:focus {
  color: #000
}

.second {
  width: 70%;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 10px 10px 5px #aaaaaa
}

.text1 {
  font-size: 15px;
  font-weight: 500;
  color: #56575b;
  font-weight: bold;
  font-family: 'Sunflower', sans-serif;
}

.text2 {
  font-size: 13px;
  font-weight: 500;
  margin-left: 6px;
  color: #e4007f;
  font-family: 'Sunflower', sans-serif;
  cursor: pointer;
}

.text3 {
  font-size: 13px;
  font-weight: 500;
  margin-right: 4px;
  margin-left: auto;
  color: #828386;
  font-family: 'Sunflower', sans-serif;
}

.collapse {
  position: relative;
  z-index: 99;
}

.reviewupdate_addtxt {
  /* padding-top: 10px;
  padding-bottom: 10px; */
  text-align: center;
  margin: auto;
  font-size: 13px;
  width: 50%;
  background-color: #fffefeee;
  font-weight: 500
}


/* 댓글 */
.comment_card {
  position: relative;
  z-index: 99;
  width: 50%;
  font-family: 'Sunflower', sans-serif;
}

.second2 {
  width: 100%;
  background-color: #f1f1f1e7;
  border-radius: 4px;
}

.comment_addtxt {
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
  margin: auto;
  font-size: 13px;
  width: 70%;
  background-color: #fffefeee;
  font-weight: 500
}

.commentupdate_addtxt {
  /* padding-top: 10px;
  padding-bottom: 10px; */
  text-align: center;
  margin: auto;
  font-size: 13px;
  width: 50%;
  background-color: #fffefeee;
  font-weight: 500
}

</style>