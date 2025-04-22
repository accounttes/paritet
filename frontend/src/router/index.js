import { createRouter, createWebHistory } from 'vue-router'
import ImageList from '../views/ImageList.vue'
import ImageUpload from '../views/ImageUpload.vue'

const routes = [
  {
    path: '/',
    name: 'ImageList',
    component: ImageList
  },
  {
    path: '/upload',
    name: 'ImageUpload',
    component: ImageUpload
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router 