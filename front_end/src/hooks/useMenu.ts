import { useMenuStore } from '@/store/menu'
import { onMounted, reactive, ref } from 'vue'

export default function (){
    const menuStore = useMenuStore()
    const sideMenu = ref([] as any)
    function getMenu(menuType: String) {
        if (menuType === 'sideMenu') {
            sideMenu.value = menuStore.sideMenu
            return menuStore.sideMenu
        }
    }

    onMounted(() => {
        getMenu('sideMenu')
        console.log('menu: ', sideMenu.value)
    })


    return { sideMenu, getMenu }
}

