<template>
  <div id="app">
    <v-app>
      <toPackHeader v-if="forbiddenPath()"></toPackHeader>
      <v-content>
        <transition name="fade" mode="out-in">
          <router-view :key="$route.fullPath"></router-view>
        </transition>
      </v-content>
    </v-app>
  </div>
</template>

<script>
  import Header from '@/components/util/Header';

  export default {
    name: 'App',
    data() {
      return {
      }
    },
    components: {
      toPackHeader: Header
    },
    methods: {
      forbiddenPath: function () {
        return !(this.$route.name === 'login' || this.$route.name === 'callback');
      }
    }
  }
</script>

<style>
  #app {
    min-height: 100vh;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .3s;
  }

  .fade-enter, .fade-leave-to {
    opacity: 0;
  }

  .v-progress-linear.progress {
    position: fixed;
    top: 0;
    left: 0;
    margin: 0;
  }

  .snackbar-progress .v-snack__wrapper {
    width: 100%;
  }

  .snackbar-progress .v-snack__content {
    height: auto !important;
    flex-wrap: wrap;
  }

  .theme--light.v-card .v-card__title.primary,
  .theme--light.v-card .v-card__title.secondary,
  .theme--light.v-card .v-card__title.warning,
  .theme--light.v-card .v-card__title.error {
    color: white;
  }

  .background {
    position: fixed;
    top: 0;
    left: 0;
    min-height: 100%;
    min-width: 100%;
    opacity: 0.7;
  }
</style>

<style lang="stylus">
  $heading-font-family = 'Lato'
  $body-font-family = 'Roboto'

  $body-bg-dark = '#323232'
  $body-bg-light = '#ffffff'

  @import '../node_modules/vuetify/src/stylus/main'
</style>
