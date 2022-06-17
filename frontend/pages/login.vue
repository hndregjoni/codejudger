<template>
  <v-content>
    <v-row justify="center" class="py-10">
      <v-row justify="center" class="pt-5">
        <v-btn class="mx-2" outlined fab color="black">
          <v-icon>mdi-github</v-icon>
        </v-btn>
        <v-btn class="mx-2" outlined fab color="red">
          <v-icon>mdi-google</v-icon>
        </v-btn>
        <v-btn class="mx-2" outlined fab color="blue">
          <v-icon>mdi-facebook</v-icon>
        </v-btn>
      </v-row>
    </v-row>
    <v-row justify="center">
      <h3>or</h3>
    </v-row>

    <v-row justify="center">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="name"
          :rules="nameRules"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :type="'password'"
          label="Password"
          required
        ></v-text-field>

        <v-row v-if="!!error">
          <v-alert dense outlined type="error">
            {{error}}
          </v-alert>
        </v-row>

        <v-row class="mt-5">
          <v-btn
            block
            fill-width
            class="ma-2 plr-3"
            outlined
            text
            color="secondary "
            @click="login()"
          >
            <h3 color="black">Log in</h3>
          </v-btn>
        </v-row>
        <v-row>
          <v-btn block class="ma-2" outlined text color="black" to="/signup" nuxt>
            Sign Up
          </v-btn>
        </v-row>
      </v-form>
    </v-row>
  </v-content>
</template>

<script>
export default {
  auth: false,

  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      (v) => !!v || "Name is required",
    ],
    password: "",
    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
    checkbox: false,

    error: undefined
  }),

  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    async login() {
      try {
        let formdata = new FormData();
        formdata.append("username", this.name);
        formdata.append("password", this.password);

        let response = await this.$auth.loginWith(
          'local',{
            data: formdata
          });
        
        await this.$auth.setUserToken(response.data.access_token)
        
        this.$router.push('/problems');
      } catch (err) {
        console.log(err);
        // Show error here!
      }
    }
  },
};
</script>
