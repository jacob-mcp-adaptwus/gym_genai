const ComponentRoutes = {
  path: '/main',
  redirect: '/components/buttons',
  component: () => import('@/layouts/component/ComponentLayout.vue'),
  children: [
    {
      name: 'TextField',
      path: '/components/textfield',
      component: () => import('@/views/forms/components/VTextField.vue')
    },
    {
      name: 'Buttons',
      path: '/components/buttons',
      component: () => import('@/views/forms/components/VButtons.vue')
    },
    {
      name: 'Autocomplete',
      path: '/components/autocomplete',
      component: () => import('@/views/forms/components/VAutocomplete.vue')
    },
    {
      name: 'Checkbox',
      path: '/components/checkbox',
      component: () => import('@/views/forms/components/VCheckbox.vue')
    },
    {
      name: 'Radio',
      path: '/components/radio',
      component: () => import('@/views/forms/components/VRadio.vue')
    },
    {
      name: 'Ratings',
      path: '/advance/ratings',
      component: () => import('@/views/ui-elements/advance/UiRatings.vue')
    },
    {
      name: 'Slider',
      path: '/components/slider',
      component: () => import('@/views/forms/components/VSlider.vue')
    },
    {
      name: 'Switch',
      path: '/components/switch',
      component: () => import('@/views/forms/components/VSwitch.vue')
    },
    {
      name: 'Avatar',
      path: '/basic/avatar',
      component: () => import('@/views/ui-elements/basic/UiAvatar.vue')
    },
    {
      name: 'Badges',
      path: '/basic/badges',
      component: () => import('@/views/ui-elements/basic/UiBadges.vue')
    },
    {
      name: 'Breadcrumb',
      path: '/basic/breadcrumb',
      component: () => import('@/views/ui-elements/basic/UiBreadcrumb.vue')
    },
    {
      name: 'Chip',
      path: '/basic/chip',
      component: () => import('@/views/ui-elements/basic/UiChip.vue')
    },
    {
      name: 'UI List',
      path: '/basic/uilist',
      component: () => import('@/views/ui-elements/basic/UiList.vue')
    },
    {
      name: 'Toltip',
      path: '/forms/plugins/tooltip',
      component: () => import('@/views/forms/plugins/tooltip/TooltipPage.vue')
    },
    {
      name: 'ExpansionPanel',
      path: '/basic/expansion-panel',
      component: () => import('@/views/ui-elements/basic/UiExpansionPanel.vue')
    },
    {
      name: 'Cards',
      path: '/basic/cards',
      component: () => import('@/views/ui-elements/basic/UiCards.vue')
    },
    {
      name: 'Tabs',
      path: '/basic/tabs',
      component: () => import('@/views/ui-elements/basic/UiTabs.vue')
    },
    {
      name: 'Alert',
      path: '/advance/alert',
      component: () => import('@/views/ui-elements/advance/UiAlert.vue')
    },
    {
      name: 'Empty State',
      path: '/advance/emptystate',
      component: () => import('@/views/ui-elements/advance/UiEmptyState.vue')
    },
    {
      name: 'Pagination',
      path: '/advance/pagination',
      component: () => import('@/views/ui-elements/advance/UiPagination.vue')
    },
    {
      name: 'Floating Action',
      path: '/advance/floatingaction',
      component: () => import('@/views/ui-elements/advance/UiFloatingAction.vue')
    },
    {
      name: 'Speed Dial',
      path: '/advance/speeddial',
      component: () => import('@/views/ui-elements/advance/UiSpeedDial.vue')
    },
    {
      name: 'Progress',
      path: '/advance/progress',
      component: () => import('@/views/ui-elements/advance/UiProgress.vue')
    },
    {
      name: 'Snackbar',
      path: '/advance/snackbar',
      component: () => import('@/views/ui-elements/advance/UiSnackbar.vue')
    },
    {
      name: 'Timeline',
      path: '/advance/timeline',
      component: () => import('@/views/ui-elements/advance/UiTimeline.vue')
    },
    {
      name: 'ButtonToggle',
      path: '/advance/btn-toggle',
      component: () => import('@/views/ui-elements/advance/UiButtonToggle.vue')
    },
    {
      name: 'Typography',
      path: '/utils/typography',
      component: () => import('@/views/utilities/typography/TypographyPage.vue')
    },
    {
      name: 'Dialog',
      path: '/forms/plugins/modal',
      component: () => import('@/views/forms/plugins/modal/DialogPage.vue')
    },
    {
      name: 'Shadows',
      path: '/utils/shadows',
      component: () => import('@/views/utilities/shadows/ShadowPage.vue')
    },
    {
      name: 'Colors',
      path: '/utils/colors',
      component: () => import('@/views/utilities/colors/ColorPage.vue')
    },
    {
      name: 'Animation',
      path: '/utils/animation',
      component: () => import('@/views/utilities/animation/AnimationPage.vue')
    },
    {
      name: 'Grid',
      path: '/utils/grid',
      component: () => import('@/views/utilities/grid/GridPage.vue')
    }
  ]
};

export default ComponentRoutes;
