import axios  from "@/plugins/axios"

const wordsStore = {
    state: {
        userWords : [],
    },

    mutations: {
        setUserWords(state, data) {
            state.userWords = data
        }
    },

    actions: {
        async fetchUserWords(context) {
            let { data } = await axios.get("/api/words-list-test/")
            context.commit("setUserWords", data)
        },

        async addWordTranslate(context, data) {
            try {
                let responce = await axios.post("/api/word-translate-list/", { "translate": data.translate, "part_of_speech": data.part_of_speech, "word": data.word })
                return responce
            }
            catch (error) {
                console.log(error);
            }
        }
    },

    getters: {
        getUserWords : state => state.userWords
    }
}

export default wordsStore;