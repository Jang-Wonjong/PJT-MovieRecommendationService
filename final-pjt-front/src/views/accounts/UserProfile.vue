<template>
  <div>

    <div class="m-4 p-3 d-flex justify-content-center" v-if="userProfile">
      <div class="card-profile p-4">
        <div class=" image d-flex flex-column justify-content-center align-items-center"> 
          <button class="btn-profile btn-secondary"> <img src="https://i.imgur.com/wvxPV9S.png" height="100" width="100" /></button>
          <span class="name mt-3">{{ userProfile.nickname }}</span> 
          <div v-if="isUpdateOn">
            <input type="text"
              v-model.trim="nicknameUpdate"
              @keyup.enter="updateProfile(userProfile)"
            >
            <button @click="updateProfile(userProfile)">SAVE</button>
          </div>
      
          <div class="d-flex flex-row justify-content-center align-items-center mt-3"> 
            <span class="number mx-3">{{ followersCounting }} <span class="follow">Followers</span></span>
            <span class="number mx-3">{{ followingsCounting }} <span class="follow">Followings</span></span> 
          </div>
          <div class=" d-flex mt-2" v-if="!isSelf"> 
            <button class="btn-profile1 btn-dark" @click="follow">Follow</button> 
          </div>
        </div>
      </div>

      <div v-if="isSelf">
        <button 
          class="btn btn-primary btn-circle btn-circle-sm m-1"
          @click="isUpdateOn=true"
          >
          <i class="fa fa-cog"></i>
        </button><br>
        <button class="btn btn-warning btn-circle btn-circle-sm m-1" @click="logout"><i class="fa fa-sign-out-alt"></i></button><br>
        <button class="btn btn-danger btn-circle btn-circle-sm m-1" @click="deleteProfile"><i class="fa fa-user-alt-slash"></i></button>
      </div>
    </div>
    

    <hr>

    <!-- movies -->
    <div class="team-grid">
      <div class="mx-5">
        <div class="intro">
          <h2 class="text-center">Movie Collection</h2>
        </div>
        <div class="row d-flex justify-content-center">
          <div class="col-md-4 col-lg-3 item" v-for="usermovie in userMovies" :key="usermovie.user_id">
            <div class="box people" :style="`background-image:url('https://image.tmdb.org/t/p/original${usermovie.poster_path}');`">
              <div class="cover" @click="moveToDetail(usermovie.movie_id)">
                <h3 class="name">{{ usermovie.title }}</h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'
// import UserMovies from '@/components/UserMovies.vue'


export default {
  name: 'UserProfile',
  // components: {
  //   UserMovies
  // },
  data: function () {
    return {
      isSelf: false,
      youId: null,
      userProfile: null,
      userMovies: null,

      isUpdateOn: false,    // 업데이트 버튼 눌렀을 때
      nicknameUpdate: null,

      isFollow: false,
      followers: null,
      followersCounting: null,
      followings: null,
      followingsCounting: null,
    }
  },
  methods: {
    ...mapActions([
      'logout',
    ]),
    getProfile: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.youId}/profile/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          
          this.userProfile = res.data
          this.getFollowers()
          this.getFollowings()
          this.getUserMovies() // 유저가 저장한 영화 불러오기
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteProfile: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/accounts/${this.youId}/profile/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('logout')
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateProfile: function (userProfile) {
      // console.log(userProfile)
      const profileItem = {
        ...userProfile,
        nickname: this.nicknameUpdate,
      }
      // console.log(profileItem)
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/${this.youId}/profile/`,
        data: profileItem,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('profileUpdate', profileItem)
          this.getProfile()
          this.isUpdateOn = false
        })
        .catch(err => {
          console.log(err)
        })
      this.nicknameUpdate = null
    },
    getUserMovies: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movie/user-movies/${this.youId}/`,
        headers: this.config
      })
        .then(res => {
          // console.log(res)
          this.userMovies = res.data
          // this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
    follow: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/follow/${this.youId}/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          // this.userMovies = res.data
          this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
    getFollowers: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/followers/${this.youId}/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.followers = res.data
          this.followersCounting = res.data.length
          // for (let i in this.followers) {
          //   if (i === this.$store.state.id) {
          //     this.isFollow = true
          //   }
          // }
          // this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
    getFollowings: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/followings/${this.youId}/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.followings = res.data
          this.followingsCounting = res.data.length
          // this.getProfile()
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
  computed: {
    ...mapGetters([
      'config',
    ])
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.youId = this.$route.query.userId
      if (this.$store.state.id == this.youId) {
      this.isSelf = true
      }
      this.getProfile()

    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style scoped>
/* profill card */
* {
  margin: 0;
  padding: 0
}

body {
  background-color: #000
}

.card-profile {
  width: 350px;
  background-color: #efefef;
  border: none;
  /* cursor: pointer; */
  transition: all 0.5s
}

.image img {
  transition: all 0.5s
}

.card-profile:hover .image img {
  transform: scale(1.5)
}

.btn-profile {
  height: 140px;
  width: 140px;
  border-radius: 50%
}

.name {
  font-size: 22px;
  font-weight: bold
}

.idd {
  font-size: 14px;
  font-weight: 600
}

.idd1 {
  font-size: 12px
}

.number {
  font-size: 22px;
  font-weight: bold
}

.follow {
  font-size: 12px;
  font-weight: 500;
  color: #444444
}

.btn-profile1 {
  height: 40px;
  width: 150px;
  border: none;
  background-color: #000;
  color: #aeaeae;
  font-size: 15px
}

.text span {
  font-size: 13px;
  color: #545454;
  font-weight: 500
}

.icons i {
  font-size: 19px
}

hr .new1 {
  border: 1px solid
}

.join {
  font-size: 14px;
  color: #a0a0a0;
  font-weight: bold
}

.date {
  background-color: #ccc
}


/* button */
.btn-circle {
  width: 45px;
  height: 45px;
  line-height: 45px;
  text-align: center;
  padding: 0;
  border-radius: 50%;
}

.btn-circle i {
  position: relative;
  top: -1px;
}

.btn-circle-sm {
  width: 35px;
  height: 35px;
  line-height: 35px;
  font-size: 0.9rem;
}

.btn-circle-lg {
  width: 55px;
  height: 55px;
  line-height: 55px;
  font-size: 1.1rem;
}

.btn-circle-xl {
  width: 70px;
  height: 70px;
  line-height: 70px;
  font-size: 1.3rem;
}

/* user movies */
body {
  background-image: linear-gradient(#3F51B5, #1A237E);
  background-repeat: no-repeat;
  color: #000;
  overflow-x: hidden
}

p {
    color: #fff
}

h2 {
    font-weight: bold;
    margin-bottom: 40px;
    padding-top: 40px;
    color: #fff
}

@media (max-width:767px) {
    h2 {
        margin-bottom: 25px;
        padding-top: 25px;
        font-size: 24px
    }
}

.intro {
    font-size: 16px;
    max-width: 500px;
    margin: 0 auto
}

.intro p {
    margin-bottom: 0
}

.people {
    padding: 50px 0;
    cursor: pointer
}

.item {
    margin-bottom: 30px
}

.item .box {
    text-align: center;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    /* width: 200px; */
    height: 300px;
    position: relative;
    overflow: hidden;
    /* object-fit: cover; */
}

.item .cover {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #d6338475;
    transition: opacity 0.15s ease-in;
    opacity: 0;
    padding-top: 80px;
    color: #fff;
    text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.15)
}

.item:hover .cover {
    opacity: 1
}

.item .name {
    font-weight: bold;
    margin-bottom: 8px
}

.item .title {
    text-transform: uppercase;
    font-weight: bold;
    color: #bbd8fb;
    letter-spacing: 2px;
    font-size: 13px;
    margin-bottom: 20px
}

.social {
    font-size: 18px
}

.social a {
    color: inherit;
    margin: 0 10px;
    display: inline-block;
    opacity: 0.7
}

.social a:hover {
    opacity: 1
}

/* .movie-detail-image {
  background-size: cover;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

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
} */
</style>