<script setup lang="ts">
import type { Form } from '#ui/types'

const addressInput = defineModel<string>('addressInput', { required: false })
const streetName = defineModel<string>('streetName', { required: false })
const streetNumber = defineModel<string>('streetNumber', { required: false })
const unitNumber = defineModel<string>('unitNumber', { required: false })
const city = defineModel<string>('city')
const postalCode = defineModel<string>('postalCode')

type AddressField = 'streetName' | 'streetNumber' | 'unitNumber' | 'streetAdditional' | 'city' | 'postalCode'

const props = defineProps<{
  id: string
  schemaPrefix: string
  formRef?: Form<any>
  disabled: boolean
  loading: boolean
}>()

const emit = defineEmits<{
  newAddress: [void]
}>()

const { address: canadaPostAddress, enableAddressComplete } = useCanadaPostAddress()

const addressComplete = (id: string) => {
  enableAddressComplete(id, 'CA', !props.disabled)
}

watch(canadaPostAddress, (newAddress) => {
  // automatically populate all non excluded / non disabled fields
  if (newAddress) {
    // clear form validation for city/region/postalCode if address is autocompleted
    if (props.formRef) {
      props.formRef.clear(`${props.schemaPrefix}streetNumber`)
      props.formRef.clear(`${props.schemaPrefix}streetName`)
      props.formRef.clear(`${props.schemaPrefix}unitNumber`)
      props.formRef.clear(`${props.schemaPrefix}city`)
      props.formRef.clear(`${props.schemaPrefix}postalCode`)
    }
    for (const key of Object.keys(newAddress)) {
      switch (key as AddressField) {
        case 'streetNumber':
          streetNumber.value = newAddress.streetNumber
          break
        case 'streetName':
          streetName.value = newAddress.streetName
          break
        case 'unitNumber':
          unitNumber.value = newAddress.unitNumber
          break
        case 'city':
          city.value = newAddress.city
          break
        case 'postalCode':
          postalCode.value = newAddress.postalCode
      }
    }

    addressInput.value = newAddress.street

    emit('newAddress')
  }
})

const addId = useId()
</script>
<template>
  <UFormGroup
    :name="schemaPrefix + 'street'"
    class="grow"
  >
    <template #default="{ error }">
      <UInput
        :id="id + '-street'"
        v-model="addressInput"
        size="lg"
        :color="addressInput ? 'primary' : 'gray'"
        :aria-label="$t('label.lookupResidentialAddress')"
        :placeholder="$t('label.lookupResidentialAddress')"
        :aria-required="true"
        :aria-invalid="error !== undefined"
        :aria-describedby="schemaPrefix + 'street-' + addId"
        :disabled="disabled"
        :loading="loading"
        class="w-full grow"
        maxlength="1000"
        @keypress.once="addressComplete(id + '-street')"
        @click="addressComplete(id + '-street')"
      />
    </template>
    <template #help>
      <span :id="schemaPrefix + 'street-' + addId">
        {{ $t('hint.autocomplete') }}
      </span>
    </template>

    <template #error="{ error }">
      <span :id="schemaPrefix + 'street-' + addId">
        {{ error }}
      </span>
    </template>
  </UFormGroup>
</template>
