<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import M from "materialize-css/dist/js/materialize.min";

export default {
  name: "app",
  mounted: function() {
    this.toaster();
  },
  methods: {
    toaster: function() {
      var myInit = { 
          method: 'GET',
          headers: new Headers(),
          mode: 'cors',
          cache: 'default'
        };
      fetch("http://127.0.0.1:8000/can_connect", myInit)
        .then(r => r.json())
        .then(() => {
          M.toast({
            html: "Connected to API",
            displayLength: 2500,
            classes: "connected rounded"
          });
        })
        .catch(() => {
          M.toast({
            html: "Fail connect to API",
            displayLength: 2500,
            classes: "error rounded"
          });
        });
    }
  }
};
</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.connected {
  background-color: #42b883 !important;
}
.error {
  background-color: rgb(220, 87, 87) !important;
}

.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}
</style>
