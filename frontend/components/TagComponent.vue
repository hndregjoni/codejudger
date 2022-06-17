<template>
<v-combobox
    :value="value"
    @input="e => bubbleUp(e)"
    :items="items"
    :label="label"
    multiple
    chips
    :required="required"
></v-combobox>
</template>

<script>
export default {
    props: {
        value: {
            default: []
        },
        label: {
            default: "Tags"
        },
        required: {
            default: false,
            type: Boolean
        }
    },

    data() {
        return {
            items: [],
        }
    },

    async fetch() {
        const response = await this.$axios.get("/tags");

        this.items = response.data.map(t => t.slug); 
    },

    mounted() {
        console.log("HEEEEEY")
        this.$fetch();
    },

    methods: {
        hello(d) {
            console.log(d);
        },

        bubbleUp(data) {
            this.$emit('input', data);
        }
    }
};
</script>