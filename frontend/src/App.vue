<template>
  <div>
    <div id="nav">
      <Navbar />
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapMutations } from "vuex"
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'app',
  components: {
    Navbar,
  },

  methods : {
    ...mapMutations(["initStore"])
  },
  mounted(){
    this.initStore()

  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

</style>
