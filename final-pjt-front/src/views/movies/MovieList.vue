<template>
  <div>
    <ul>
      <li v-for="movie in movies" :key="movie.id">
        <span>{{ movie.title }}</span>
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
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        // headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.movies = res.data
          // console.log(this.movies[0].tmdb_id)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>

</style>