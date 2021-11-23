<template>
  <div>
    <h1>RecommendUser</h1>
    <div v-for="recomUser in recomUsers" :key="recomUser[1]">
      <p @click="moveToProfile(recomUser[1])">{{ recomUser }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'


export default {
  name: 'RecommendUser',
  data: function () {
    return {
      recomUsers: null,
    }
  },
  methods: {
    getRecomend: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movie/recommend-user/',
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.recomUsers = res.data
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
    },
  },
  computed: {
    ...mapGetters([
      'config',
    ])
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getRecomend()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style>

</style>