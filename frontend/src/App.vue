<template>
  <div>
    <div id="nav">
      <Navbar />
    </div>
    <router-view/>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'app',
  components: {
    Navbar,
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
