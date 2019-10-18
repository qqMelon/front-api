<template>
    <div class="dashboard">
      <!-- <a class="btn-floating btn-large waves-effect waves-light tile pulse" @click="goHome"><i class="material-icons">home</i></a> -->
      <h1>ALLLOOOO</h1>
    </div>
</template>

<script>
export default {
  name: "dashboard",
  methods: {
    goHome: function() {
      this.$router.push({ name: "home" })
    }
  }
};
</script>

<style lang="scss" scoped>
.dashboard {
    height: 100vh;
    background-image: url(https://images.pexels.com/photos/417458/pexels-photo-417458.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260);
    background-position: cover;

    .btn-floating {
      position: absolute;
      bottom: 45px;
      right: 45px;
    }
}
</style>