<template>
  <div>
    <section class="wrapper">
      <div class="container">
  
        <div class="row">
          <div class="col-md-4">
            <div class="card text-white card-has-bg click-col" style="background-image:url('https://source.unsplash.com/600x900/?tech,street');">
              <img class="card-img d-none" src="https://source.unsplash.com/600x900/?tech,street" alt="Goverment Lorem Ipsum Sit Amet Consectetur dipisi?">
              <div class="card-img-overlay d-flex flex-column">
                <div class="card-body">
                  <small class="card-meta mb-2">Thought Leadership</small>
                    <h4 class="card-title mt-0 "><a class="text-white" herf="#">Goverment Lorem Ipsum Sit Amet Consectetur dipisi?</a></h4>
                  <small><i class="far fa-clock"></i> October 15, 2020</small>
                </div>
                <div class="card-footer">
                  <div class="media">
                    <img class="mr-3 rounded-circle" src="https://cdn0.iconfinder.com/data/icons/user-pictures/100/male-512.png" alt="Generic placeholder image" style="max-width:50px">
                    <div class="media-body">
                      <h6 class="my-0 text-white d-block">Oz COruhlu</h6>
                      <small>Director of UI/UX</small>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
  <!-- <div>
    <ul>
      <li v-for="movie in movies" :key="movie.id" class="liTag">
        <span @click="moveToDetail(movie.id)">{{ movie.title }}</span>
      </li>
    </ul>
  </div> -->
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
          // console.log(res)
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToDetail: function (movieId) {
      console.log(movieId)
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

<style scoped>
.liTag {
  cursor: pointer;
}

.liTag:hover {
  background-color: #d63384;
}
</style>