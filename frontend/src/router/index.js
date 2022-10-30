import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import NotesView from '@/views/NotesView.vue'
import store from '@/store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/log-in',
    name: 'login',
    component: LoginView
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/notes',
    name: 'notes',
    component: NotesView,
		meta: {
				loginRequired: true
		}
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
		to.matched.some((record) => {
				if (record.meta.loginRequired && !store.state.isAuthenticated){
						next('/log-in')
				} else {
						next()
				}
		})
})

export default router
