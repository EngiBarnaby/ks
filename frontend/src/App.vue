<template>
  <div>
    <div id="nav">
      <Navbar />
      <HomePage />
    </div>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue'
import HomePage from '@/components/HomePage.vue'

export default {
  name: 'app',
  components: {
    Navbar,
    HomePage,
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
