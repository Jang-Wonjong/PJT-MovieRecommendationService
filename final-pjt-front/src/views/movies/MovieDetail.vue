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
      <span>{{ reviews }}</span>
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
          console.log(res)
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
          console.log(res)
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
          console.log(res)
          this.reviews += res.data
          this.getReviews()
        })
        .catch(err => {
          console.log(err)
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
    imgSrc: function () {
      return 'https://image.tmdb.org/t/p/w400' + this.SelectedMovie.poster_path
    }
  }
}
</script>

<style>

</style>