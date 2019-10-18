<template>
  <div class="dashboard">
    <a
      class="btn-floating btn-large waves-effect waves-light tile pulse"
      @click="goHome"
      ><i class="material-icons">home</i></a
    >
    <div class="dashboard-container row">
      <!-- <div class="left-container col s6"></div>
      <div class="right-container col s6"></div> -->
      {{ unicorns }}
      <button @click="callData">Bonjour</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "dashboard",
  data: function() {
    return {
      unicorns: null,
      feedBack: ""
    };
  },
  // mounted: function() {
  //   this.callData();
  // },
  methods: {
    goHome: function() {
      this.$router.push({ name: "home" });
    },
    callData: function() {
      const myInit = {
        method: "GET",
        headers: {
          Accept: "application/json, text/plain, */*",
          "Content-Type": "application/json"
        },
        cache: "default"
      };
      fetch("http://127.0.0.1:8000/unicorns/1", myInit)
        .then(response => response.json())
        .then(data => {
          console.log(data);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.dashboard {
  height: 100vh;
  background-image: url(https://images.pexels.com/photos/2096578/pexels-photo-2096578.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940);
  background-position: cover;
  display: flex;
  justify-content: center;
  align-items: center;

  .btn-floating {
    position: absolute;
    bottom: 45px;
    right: 45px;
  }

  .dashboard-container {
    width: 80%;
    height: 80%;
    background-color: aliceblue;
  }
}
</style>
