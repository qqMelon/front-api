<template>
  <div class="home">
    <a class="btn-floating btn-large waves-effect waves-light tile pulse" @click="goDashboard"><i class="material-icons">dashboard</i></a>
    <div class="loger-container">
      <div class="head-loger-content">
        <div
          class="btn-custom btn-to-login"
          :class="{ active: inLogin }"
          @click="toLogin"
        >
          Login
        </div>
        <div
          class="btn-custom btn-to-register"
          :class="{ active: inRegister }"
          @click="toRegister"
        >
          Register
        </div>
      </div>
      <div class="body-loger-content">
        <transition name="slide-fade" mode="out-in">
          <Login v-if="inLogin" @logData="sendData" />
          <Register v-else />
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";

export default {
  name: "home",
  components: {
    Login,
    Register
  },
  data: function() {
    return {
      inLogin: true,
      inRegister: false
    };
  },
  methods: {
    toLogin: function() {
      if (this.inLogin) {
        return;
      } else {
        this.inLogin = true;
        this.inRegister = false;
      }
    },
    toRegister: function() {
      if (this.inRegister) {
        return;
      } else {
        this.inLogin = false;
        this.inRegister = true;
      }
    },
    goDashboard: function() {
      this.$router.push({ name: "dashboard" })
    },
    sendData: function(data) {
      console.log(data); // eslint-disable-line no-console
    }
  }
};
</script>

<style lang="scss" scoped>
.home {
  height: 100vh;
  background-image: url(https://images.pexels.com/photos/669996/pexels-photo-669996.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940);
  display: flex;
  justify-content: center;
  align-items: center;

  .btn-floating {
    position: absolute;
    bottom: 45px;
    right: 45px;
  }

  .loger-container {
    width: 350px;
    height: 450px;
    background-color: aliceblue;

    .head-loger-content {
      width: 100%;
      height: 45px;
      display: flex;
      flex-direction: row;

      .btn-custom {
        width: 50%;
        border-radius: 0;
        background-color: #94ceca;
        display: flex;
        justify-content: center;
        align-items: center;
        color: aliceblue;
        cursor: pointer;

        &.active {
          background-color: #14868c !important;
        }
      }
    }

    .body-loger-content {
      padding: 25px;
      margin-top: 35px;
    }
  }
}
</style>
