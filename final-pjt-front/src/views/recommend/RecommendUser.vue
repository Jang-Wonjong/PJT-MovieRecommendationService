<template>
  <div>
    <div class="container py-5">
      <div class="row text-center text-white">
        <div class="col-lg-8 mx-auto">
          <h1 class="display-4 h1Tag">Let's Movie and Chill</h1>
            <p class="lead mb-1 text1">나와 취향이 비슷한 친구의 컬렉션에서 영화를 추천 받으세요!</p>
            <p class="lead mb-0 text1">추천이 없다면 먼저 내 컬렉션에 좋아하는 영화를 넣어보세요</p>
            <!-- <span>{{recomUsers}}</span> -->
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row text-center">
        <div class="col-xl-3 col-sm-6 mb-5" v-for="recomUser in recomUsers" :key="recomUser.id">
          <div class="bg rounded shadow-sm py-5 px-4">
            <img 
              src="https://bootstrapious.com/i/snippets/sn-team/teacher-4.jpg" alt="" 
              width="100" 
              class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm pointer"
              @click="moveToProfile(recomUser.id)"
            >
            <h5 class="mb-3 h1Tag pointer">{{ recomUser.nickname }}</h5>
            <span class="text1">함께 좋아하는 영화</span><br>
            <span class="text1">{{ recomUser.same_cnt }}</span>
          </div>
        </div>
      </div>
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
      slides: [
        {
          title: 'Slide #1',
          content: 'Slide content.'
        }
      ],
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
          // console.log(res)
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

<style scoped>
.bg {
  background-color: black;
  opacity: 0.7;
}

.bg-t {
  background-color: black;
  opacity: 0.7;
}

.h1Tag {
  color: white;
  font-family: 'Noto Sans KR', sans-serif;
}

.text1 {
  font-size: 15px;
  font-weight: 500;
  color: #dddddd;
  font-weight: bold;
  font-family: 'Sunflower', sans-serif;
}

.pointer {
  cursor: pointer;
}
</style>