<template>
		<NavbarComp @logout="logout" />
		<my-message @closeMessage="closeMessage" v-if="showMessages" :messages="messages"/>
		<section class="section">
				<router-view />
		</section>
		<SiteFooter />
</template>
<script>
import axios from 'axios';
import NavbarComp from '@/components/NavbarComp.vue';
import SiteFooter from '@/components/SiteFooter.vue';
export default {
		data(){
				return {
						messages: [],
						showMessages: false
				}
		},
		components: {
				NavbarComp, SiteFooter
		},
		beforeCreate(){
				this.$store.commit('initializeStore')
				const token = this.$store.state.token

				if (token){
						axios.defaults.headers.common['Authorization'] = "Token " + token
				} else {
						axios.defaults.headers.common['Authorization'] = ""
				}
		},
		methods: {
				logout(){
						axios
								.post('api/v1/token/logout')
								.then(res => {
										localStorage.removeItem('token')
										axios.defaults.headers.common['Authorization'] = ""
										this.$store.commit('removeToken')
										this.$router.push('/log-in')
								})
								.catch(error => {
										this.messages.push(error.message)
										for (const key in error.response.data){
												for (var i = 0; i < error.response.data[key].length; i++){
														this.messages.push(error.response.data[key][i])	
												}
										}
										this.showMessages = true
								})
				},
				closeMessage(){
						this.messages = []
						this.showMessages = false
				}
		}
}
</script>
<style lang="scss">
@import '../node_modules/bulma'
</style>
