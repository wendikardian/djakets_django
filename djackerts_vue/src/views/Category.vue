<template>
    <div class="page-category">
        <div class="columns is-multiline has-text-centered">
            <h2 class="is-size-2 has-text-centered">
                {{category.name}}
            </h2>
        </div>
        <div class="column is-3" v-for="product in category.products" v-bind:key="product.id">
            <div class="box">
              <figure class="image mb-4">
                <img :src="product.get_thumbnail" >
              </figure>
    
              <h3 class="is-size-4">{{product.name}}</h3>
              <p class="is-size-6 has-text-grey">$ {{product.price}}</p>
    
              <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4"> 
                View Details
              </router-link>
            </div>
          </div>
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default{
    name : 'Category',
    data(){
        return{
            category : {
                products : []
            }
        }
    },
    mounted(){
        this.getCategory()
    }, methods : {
        async getCategory(){
            const categorySlug = this.$route.params.category_slug
            this.$store.commit('setIsLoading', true)
            await axios.get(`/api/v1/products/${categorySlug}`)
            .then(res => {
                this.category = res.data
                document.title = this.category.name + '| Djackets'
            } ).catch(err => {
                console.error(err)
            })
            
            toast({
                message: `Summer is opened`,
                type: 'is-success',
                position: 'top-right',
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: 'bottom-right'
            })

             this.$store.commit('setIsLoading', false)

        }
    }
}

</script>