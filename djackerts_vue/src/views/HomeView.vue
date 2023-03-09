<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to Djacket</p>
        <p class="subtitle">The Best Jacket Store online :D</p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <product-box
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import productBox from '@/components/productBox.vue';
export default {
  name: "Home",
  data() {
    return{
      latestProducts : []
    }
  },
  components: {
    productBox
  },
  mounted() {
    this.getLatestProducts()
    document.title = 'Home | Djackets'
  },
  methods : {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)
      await axios.get('/api/v1/latest-products').then(res => {
        this.latestProducts = res.data
      }).catch(err => console.error(err))
      this.$store.commit('setIsLoading', false)
    }
  }
};
</script>


