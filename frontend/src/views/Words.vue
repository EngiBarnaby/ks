<template>
    <div>
        <p>
            {{ this.getUserWords }}
        </p>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex"
export default {
    name : "Words",

    methods : {
        ...mapActions(["fetchUserWords"])
    },

    computed : {
        ...mapGetters(["getUserWords"])
    },

    async mounted(){
        await this.fetchUserWords()
    }
    
}

</script>
