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
        <i class="material-icons prefix">contact_mail</i>
        <input
          id="icon_email"
          type="text"
          class="validate"
          v-model="inputMail"
        />
        <label for="icon_email">Email</label>
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
        :class="{ pulse: readyToSend() }"
        type="submit"
        name="action"
      >
        Register DataLogin
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
      inputMail: "",
      inputPass: ""
    };
  },
  methods: {
    readyToSend: function() {
      if (
        this.inputPass !== "" &&
        this.inputPass !== "" &&
        this.inputMail !== ""
      ) {
        return true;
      } else {
        return false;
      }
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
