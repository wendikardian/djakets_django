<template>
  <div class="page-category">
    <div class="columns is-multiline has-text-centered">
      <h2 class="is-size-2 has-text-centered">
        {{ category.name }}
      </h2>
    </div>
    <product-box
        v-for="product in category.products"
        v-bind:key="product.id"
        v-bind:product="product" />
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import productBox from "@/components/productBox.vue";

export default {
  name: "Category",
    components: {
        productBox,
    },
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  mounted() {
    this.getCategory();
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;
      this.$store.commit("setIsLoading", true);
      await axios
        .get(`/api/v1/products/${categorySlug}`)
        .then((res) => {
          this.category = res.data;
          document.title = this.category.name + "| Djackets";
        })
        .catch((err) => {
          console.error(err);
        });

      toast({
        message: `Summer is opened`,
        type: "is-success",
        position: "top-right",
        dismissible: true,
        pauseOnHover: true,
        duration: 3000,
        position: "bottom-right",
      });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
