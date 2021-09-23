<template>
    <div class="box ml-1">
        <div class="content">
            <h5 class="has-text-centered">
                {{ word.content }}
            </h5>
            <div class="part-of-speech">
                <h5>
                    {{word.part_of_speech}}
                </h5>
            </div>
            <p class="has-text-centered word">
                Translate
            </p>

            <div v-for="wordTranslate in word.words_translate" :key="wordTranslate.id">
                <p>
                    {{ wordTranslate.translate }}
                </p>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props : {
        word : {
            type : Object,
            required : true,
        }
    },

    name : "WordList"
}
</script>

<style lang="scss">

.box {
    position: relative;
    border: 1px solid rgb(112, 135, 153);
}

.word {
    border-bottom: 1px solid black;
}

.part-of-speech {
    position: absolute;
    // width: 40px;
    // height: 30px;
    // border: 1px solid rgb(112, 135, 153);
    top:  5px;
    left: 5px;
    padding-left: 3px;
}

</style>
