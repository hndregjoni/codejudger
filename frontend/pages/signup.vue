<template>
  <!-- <div v-if="value1" > -->
  <v-content v-if="value1" fill-height fluid>
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
          v-model="username"
          label="Username"
          :counter="80"
          :error-messages="errors"
          required
        ></v-text-field>

        <v-text-field
          v-model="email"
          :type="'email'"
          label="Email"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :type="'password'"
          :rules="passwordRules"
          label="Password"
          required
        ></v-text-field>

        <v-text-field
          v-model="confirmPassword"
          :type="'password'"
          :rules="[
            [(v) => !!v || 'Password is required'],
            this.password === this.confirmPassword || 'Password must match',
          ]"
          label="Confirm password"
          required
        ></v-text-field>

        <v-row class="mt-5"> </v-row>
        <v-row>
          <v-btn
            @click="(value1 ^= true), (value2 ^= true)"
            block
            class="btn"
            outlined
            text
            color="black"
          >
            Next
          </v-btn>
        </v-row>
      </v-form>
    </v-row>
  </v-content>

  <v-content v-else-if="value2" class="pb-10">
    <v-row justify="center">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="full_name"
          :rules="nameRules"
          label="Full name"
          required
        ></v-text-field>

        <v-select
          placeholder="0"
          class="gender pa-0"
          v-model="gender"
          :items="[
            { text: 'Male', value: 1 },
            { text: 'Female', value: 2 },
            { text: 'Other', value: 3 },
            { text: 'Not specified', value: 4 },
          ]"
          label="Gender"
          required
        ></v-select>

        <v-label>Bio</v-label>

        <v-textarea counter="90" v-model="bio" solo required></v-textarea>

        <tag-component v-model="interests" :label="Interests" required />

        <v-row class="mt-5">
          <input
            type="text"
            onkeypress="return event.charCode >= 48 && event.charCode <= 57"
            required
          />
        </v-row>
        <v-row v-if="!!error">
          <v-alert dense outlined type="error">
            {{error}}
          </v-alert>
        </v-row>
        <v-row>
          <v-btn
            @click="signUp"
            v-show="value2"
            block
            class="btn mb-2"
            outlined
            text
            color="black"
            type="submit"
          >
            Sign up
          </v-btn>

          <v-btn
            @click="secondPage"
            v-show="value1"
            block
            class="btn"
            outlined
            text
            color="black"
          >
            Next
          </v-btn>

          <v-btn
            @click="firstPage"
            v-show="value2"
            block
            class="btn"
            outlined
            text
            color="black"
          >
            Previous
          </v-btn>
        </v-row>
      </v-form>
    </v-row>
  </v-content>
</template>

<script>
import TagComponent from "../components/TagComponent.vue";
export default {
  components: { TagComponent },
  auth: false,

  data() {
    return {
      name: "",
      password: "",
      full_name: "",
      interests: ["c"],
      bio: "",
      value1: true,
      value2: false,

      error: undefined
    };
  },
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

    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },

    secondPage() {
      this.value1 = false;
      this.value2 = true;
    },

    firstPage() {
      this.value1 = true;
      this.value2 = false;
    },

    async signUp(e) {
      e.preventDefault();

      if (!this.$refs.form.validate()) return;

      const obj = {
        username: this.username,
        password: this.password,
        email: this.email,
        gender: this.gender,
        full_name: this.full_name,
        interests: this.interests,
        bio: this.bio,
      };

      try {
        let result = await this.$axios.post("users/", obj);

        this.$router.push("/login")
      } catch (e) {
        this.error = "There was an error signing up!";
      }
    },
  },
};
</script> 