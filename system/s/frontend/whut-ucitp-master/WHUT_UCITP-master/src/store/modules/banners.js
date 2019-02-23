import api from '@/utils/axios'

const state = {
    status:'normal',
    bannerList:[]
}

const getters = {
    banners:state =>{
        return state.banners.bannerList
    }
}

const mutations = {
    SET_BANNER_LIST(state,data) {
        state.bannerList = data
    },
    GET_BANNER_LIST ({ commit }) {
        api.mock('/banners')
        .then(res => {
            console.log(res);
            commit('SET_BANNER_LIST',res.banners);
        })
    }
}

const actions = {
    GET_BANNER_LIST ({ commit }) {
        api.mock('/banners')
        .then(res => {
            console.log(res);
            commit('SET_BANNER_LIST',res.banners);
        })
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
/*

const bannerList = {
    state:{
        status:'normal',
        banners:[]
    },
    mutations:{
        SET_BANNERS(state,data) {
            console.log(data)
            state.banners = data
        }
    }
}

export default bannerList

*/