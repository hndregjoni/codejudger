<template>
  <span v-if="(roles===undefined && this.$store.state.auth.loggedIn) || 
        (roles !== undefined && !(roles.length > 0) 
            || (this.$store.state.auth.loggedIn && 
                roles.every(r=>this.$store.state.auth.user.roles.includes(r))))" 
                :key="roles">
    <slot></slot>
  </span>
</template>
<script>
export default {
  // prob: ()=>{

  // }
  props: {
    roles: {
      type: Array,
      default: undefined,
    },
  },
};
</script>