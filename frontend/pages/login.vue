<template>

<v-container fill-height fluid >
  
    
  <v-row  justify="center" class="py-10" >

    <v-row justify="center" class="pt-5 ">
   <v-btn 
      class="mx-2"
      outlined
      fab
      color="black"
    >
      <v-icon>mdi-github</v-icon>
    </v-btn>
    <v-btn 
      class="mx-2"
      outlined
      fab
      color="red"
    >
      <v-icon>mdi-google</v-icon>
    </v-btn>
    <v-btn 
      class="mx-2"
      outlined
      fab
      color="blue"
    >
      <v-icon>mdi-facebook</v-icon>
    </v-btn>
    </v-row>
  </v-row>
  <v-row justify="center" >
    <h3>or</h3>
  </v-row>

  <v-row  justify="center">
     
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Username"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :type="'password'"
      :rules="emailRules"
      label="Password"
    
      required
    ></v-text-field>


    <v-row class ="mt-5" >
      <v-btn 
        block
        fill-width
        class="ma-2 plr-3 "
        outlined
        text
        color="secondary "   
      >
      <h3 color="black">
         Log in 
      </h3  >
    
    </v-btn>

    </v-row>
      <v-row >
          <v-btn
            block
            class="ma-2"
            outlined
            text
            color="black"
          >
          Sign in 
        </v-btn>
  </v-row>
    



  </v-form>  

  </v-row>
 
</v-container>

    
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      checkbox: false,
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
  }
</script>
