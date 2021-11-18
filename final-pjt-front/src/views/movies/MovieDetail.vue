<template>
  <div>
    <h1>DETAIL~~~</h1>
    <span>{{ movie }}</span>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie: null,
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
        url: `http://127.0.0.1:8000/movie/${this.$route.query.movieId}`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.movie = res.data
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovie()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>