<template>
  <div>
    <ul>
      <li v-for="movie in movies" :key="movie.id">
        <span @click="moveToDetail(movie.id)">{{ movie.title }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieList',
  data: function () {
    return {
      movies: null,
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
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movie/list/',
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToDetail: function (movieId) {
      // console.log(movieId)
      this.$router.push({
        name: 'MovieDetail',
        query: { movieId }  
      })
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>