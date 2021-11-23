<template>
  <div>
    <section class="wrapper">
      <div class="container">
        <div class="row">
          <div class="col-md-3 d-flex" v-for="movie in movies" :key="movie.id">
            <div class="card text-white card-has-bg click-col" :style="`background-image:url('https://image.tmdb.org/t/p/w400${movie.poster_path}');`">
              <img class="card-img d-none" :src="`https://image.tmdb.org/t/p/w400${movie.poster_path}`" alt="movie_poster">
              <div class="card-img-overlay d-flex flex-column movie-font" @click="moveToDetail(movie.id)">
                <div class="card-body">
                  <small class="card-meta mb-2">{{ movie.original_title }}</small>
                </div>
                <div class="card-footer">
                  <h4 class="card-title mt-0 fs-6">{{ movie.title }}</h4>
                  <!-- <small><i class="far fa-clock"></i>{{ movie.release_date }}</small> -->
                  <!-- <div class="media">
                    <img class="mr-3 rounded-circle" src="https://cdn0.iconfinder.com/data/icons/user-pictures/100/male-512.png" alt="Generic placeholder image" style="max-width:50px">
                    <div class="media-body">
                      <h6 class="my-0 text-white d-block">Oz COruhlu</h6>
                      <small>Director of UI/UX</small>
                    </div>
                  </div> -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'


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
        url: 'http://127.0.0.1:8000/movie/list/',
        headers: this.config
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
  },
  computed: {
    ...mapGetters([
      'config',
    ]),
  },
}
</script>

<style scoped> 
.liTag {
  cursor: pointer;
}

.liTag:hover {
  background-color: #d63384;
}

.movie-font {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>