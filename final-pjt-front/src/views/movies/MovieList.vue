<template>
  <div>
    <section class="wrapper">
      <!-- <div class="container"> -->
        <div class="row">
          <div class="col-md-3 d-flex mt-4 mx-auto" v-for="movie in movies" :key="movie.id">
            <div class="card text-white card-has-bg click-col" :style="`background-image:url('https://image.tmdb.org/t/p/w400${movie.poster_path}');`">
              <img class="card-img d-none" :src="`https://image.tmdb.org/t/p/w400${movie.poster_path}`" alt="movie_poster">
              <div class="card-img-overlay d-flex flex-column movie-font" @click="moveToDetail(movie.id)">
                <div class="card-body">
                  <div class="original-title-tag">
                  <span class="card-meta mb-2">{{ movie.original_title }}</span>
                  </div>
                </div>
                <!-- <div class="card-footer">
                  <h4 class="card-title mt-0 fs-4">{{ movie.title }}</h4> -->
                  <!-- <small><i class="far fa-clock"></i>{{ movie.release_date }}</small> -->
                  <!-- <div class="media">
                    <img class="mr-3 rounded-circle" src="https://cdn0.iconfinder.com/data/icons/user-pictures/100/male-512.png" alt="Generic placeholder image" style="max-width:50px">
                    <div class="media-body">
                      <h6 class="my-0 text-white d-block">Oz COruhlu</h6>
                      <small>Director of UI/UX</small>
                    </div>
                  </div> -->
                <!-- </div> -->
              </div>
            </div>
          </div>
        </div>
      <!-- </div> -->
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



/* card */
body {
  background-color: #FCBF49;
}

.wrapper {
  margin: 10vh;
}

.card {
  width: 500px;
  border: none;
  transition: all 500ms cubic-bezier(0.19, 1, 0.22, 1);
  overflow: hidden;
  border-radius: 20px;
  min-height: 450px;
  box-shadow: 0 0 12px 0 rgba(0, 0, 0, 0.2);
}
@media (max-width: 768px) {
  .card {
    min-height: 350px;
  }
}
@media (max-width: 420px) {
  .card {
    min-height: 300px;
  }
}
.card.card-has-bg {
  transition: all 500ms cubic-bezier(0.19, 1, 0.22, 1);
  background-size: 120%;
  background-repeat: no-repeat;
  background-position: center center;
}
.card.card-has-bg:before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  /* background: inherit; */
  -webkit-filter: grayscale(1);
  -moz-filter: grayscale(100%);
  -ms-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  filter: grayscale(100%);
}
.card.card-has-bg:hover {
  transform: scale(0.98);
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.3);
  background-size: 130%;
  transition: all 500ms cubic-bezier(0.19, 1, 0.22, 1);
}
.card.card-has-bg:hover .card-img-overlay {
  transition: all 800ms cubic-bezier(0.19, 1, 0.22, 1);
  background: #234f6d;
  background: linear-gradient(0deg, #faf8f975 100%, #444344 0%);
}
.card .card-footer {
  background: none;
  border-top: none;
}
.card .card-footer .media img {
  border: solid 3px rgba(234, 95, 0, 0.3);
}
.card .card-meta {
  color: orange;
  font-size: 17px;
  /* background-color:rgba(0, 0, 0, 0.3);
  opacity: 0.5; */
}
.card .card-body {
  transition: all 500ms cubic-bezier(0.19, 1, 0.22, 1);
}
.card:hover {
  cursor: pointer;
  transition: all 800ms cubic-bezier(0.19, 1, 0.22, 1);
}
.card:hover .card-body {
  margin-top: 30px;
  transition: all 800ms cubic-bezier(0.19, 1, 0.22, 1);
}
.card .card-img-overlay {
  transition: all 800ms cubic-bezier(0.19, 1, 0.22, 1);
  background: #000000;
  background: linear-gradient(0deg, rgba(255, 255, 255, 0) 0%, #77777780 100%);
}

.card-title {
  background-color: black;
  opacity: 0.7;
  color: white;
  font-family: 'Noto Sans KR', sans-serif;
}

.original-title-tag{
  background-color: black;
  opacity: 0.6;
  padding-top: 2px;
  padding-bottom: 2px;
}

</style>