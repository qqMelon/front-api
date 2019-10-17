<template>
  <div class="login">
    <div class="row">
      <div class="input-field">
        <i class="material-icons prefix">account_circle</i>
        <input
          id="icon_prefix"
          type="text"
          class="validate"
          v-model="inputId"
        />
        <label for="icon_prefix">ID</label>
      </div>
      <div class="input-field">
        <i class="material-icons prefix">https</i>
        <input
          id="icon_telephone"
          type="password"
          class="validate"
          v-model="inputPass"
        />
        <label for="icon_telephone">Password</label>
      </div>
      <button
        class="btn waves-effect waves-light"
        type="submit"
        name="action"
        @click.prevent="log"
      >
        Send DataLogin
        <i class="material-icons right">send</i>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data: function() {
    return {
      inputId: "",
      inputPass: ""
    };
  },
  methods: {
    log: function() {
      let data = { id: this.inputId, pass: this.inputPass };
      this.$emit("logData", data);
    }
  }
};
</script>

<style lang="scss" scoped>
.login {
  .row {
    .btn {
      margin-top: 15px;
      width: 100%;
    }
  }
}
</style>
