// useIspValue.js
import { ref, onMounted } from 'vue';

export function useIspValue() {
  const ispValue = ref(false);

  onMounted(() => {
    const params = new URLSearchParams(window.location.search);
    const isp = params.get('isp');
    ispValue.value = isp !== null && parseInt(isp) === 1;
  });

  return { ispValue };
}
