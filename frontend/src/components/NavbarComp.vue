<template>
		<div class="navbar has-shadow is-white">
				<!--Navbar brand-->
				<div class="navbar-brand">
						<div class="navbar-item">
								<router-link class="has-text-black" to="/">
										NotesApp
								</router-link>
						</div>
						<a 
						@click="toggleBurger"
						class="navbar-burger" 
						:class="{'is-active': showBurger}">
								<span aria-hidden="true"></span>
								<span aria-hidden="true"></span>
								<span aria-hidden="true"></span>
						</a>
				</div>

				<!--Navbar menu-->
				<div class="navbar-menu" :class="{'is-active': showBurger}">
						<!--Start-->
						<div class="navbar-start">
								<router-link
									 @click="toggleBurger"
										to="/"			
										class="navbar-item is-size-4"
								>
									Home	
								</router-link>
								<router-link
									 @click="toggleBurger"
									 v-if="this.$store.state.isAuthenticated"
										to="/notes"			
										class="navbar-item is-size-4"
								>
									Notes	
								</router-link>
						</div>
						<!--End with buttons-->
						<div class="navbar-end">
								<div class="navbar-item">
										<div class="buttons">
												<a
													 v-if="this.$store.state.isAuthenticated"
													 @click="$emit('logout')"
														class="button is-light"
												>
													Logout	
												</a>
												<router-link
													 v-if="!this.$store.state.isAuthenticated"
													 @click="toggleBurger"
														to="/sign-up"			
														class="button is-primary"
												>
													Sign-up	
												</router-link>
												<router-link
													 v-if="!this.$store.state.isAuthenticated"
													 @click="toggleBurger"
														to="/log-in"			
														class="button is-light"
												>
													Log-in	
												</router-link>
										</div>
								</div>
						</div>
				</div>
		</div>
</template>

<script>
export default {
		data(){
				return {
						showBurger: false
				}
		},
		methods: {
				toggleBurger(){
						this.showBurger = !this.showBurger
				}
		}	
}
</script>

<style scoped>

</style>
