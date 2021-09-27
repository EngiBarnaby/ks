import axios from "@/plugins/axios"

const wordsStore = {
    state: {
        userWords: [],
        nextPage: "",
        prevPage: "",
        countWords: 0,
    },

    mutations: {
        setUserWords(state, data) {
            state.userWords = data.results
            state.countWords = data.count
            state.nextPage = data.next
            state.prevPage = data.previous
        }
    },

    actions: {
        async fetchUserWords(context, query) {
            let { data } = await axios.get(`/api/words-list-test/?page=${query.pageNum}&page_size=${query.page_size}`)
            console.log(data);
            context.commit("setUserWords", data)
        },

        async nextWords(context) {
            await axios({ method: "GET", url: context.state.nextPage })
                .then(res => {
                context.commit("setUserWords", res.data)
            })
        },

        async prevWords(context) {
            await axios({ method: "GET", url: context.state.prevPage })
                .then(res => {
                context.commit("setUserWords", res.data)
            })
        },

        async addWordTranslate(context, data) {
            try {
                return await axios.post("/api/word-translate-list/", { "translate": data.translate, "part_of_speech": data.part_of_speech, "word": data.word })
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