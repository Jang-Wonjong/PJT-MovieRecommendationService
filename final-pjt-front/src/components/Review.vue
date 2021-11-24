<template>
  <div class="justify-content-center mt-5 border-left border-right body">
    <div class="d-flex justify-content-center pt-3 pb-2"> <input type="text" name="text" placeholder="+ Add a note" class="form-control addtxt"></div>
      <div class="d-flex justify-content-center py-2">
        <div class="second py-2 px-2"> <span class="text1">Type your note, and hit enter to add it</span>
          <div class="d-flex justify-content-between py-1 pt-2">
            <div><img src="https://i.imgur.com/AgAC1Is.jpg" width="18"><span class="text2">Martha</span></div>
            <div><span class="text3">Upvote?</span><span class="thumbup"><i class="fa fa-thumbs-o-up"></i></span><span class="text4">3</span></div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Review',
  props: {
    MovieDetail: Object
  }
}
</script>

<style scoped>
/* 리뷰리뷰리뷰리뷰리뷰리뷰리뷰리뷰 */
.body {
    background-color: rgba(255, 255, 255, 0.493);
    position: relative;
    z-index: 99;
}

/* .review_container {
    background-color: #eef2f5;
    width: 400px;
    position: relative;
    z-index: 99;
} */

.addtxt {
    padding-top: 10px;
    padding-bottom: 10px;
    text-align: center;
    font-size: 13px;
    width: 350px;
    background-color: #e5e8ed;
    font-weight: 500
}

.form-control:focus {
    color: #000
}

.second {
    width: 350px;
    background-color: white;
    border-radius: 4px;
    box-shadow: 10px 10px 5px #aaaaaa
}

.text1 {
    font-size: 13px;
    font-weight: 500;
    color: #56575b
}

.text2 {
    font-size: 13px;
    font-weight: 500;
    margin-left: 6px;
    color: #56575b
}

.text3 {
    font-size: 13px;
    font-weight: 500;
    margin-right: 4px;
    color: #828386
}

.text3o {
    color: #00a5f4
}

.text4 {
    font-size: 13px;
    font-weight: 500;
    color: #828386
}

.text4i {
    color: #00a5f4
}

.text4o {
    color: white
}

.thumbup {
    font-size: 13px;
    font-weight: 500;
    margin-right: 5px
}

.thumbupo {
    color: #17a2b8
}
</style>