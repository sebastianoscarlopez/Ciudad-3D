import { createSlice } from '@reduxjs/toolkit'

const alerts = createSlice({
  name: 'alerts',
  initialState: {
    ids: [],
    extraData: {},
    showModalAlert: false,
    showModalAlertId: ''
  },
  reducers: {
    addId: (draftState, { payload: id }) => {
      if (!draftState.ids.includes(id)) {
        draftState.ids.push(id)
      }
    },
    addExtraData: (draftState, { payload: { id, titleSuffix, value } }) => {
      draftState.extraData[id] = draftState.extraData[id] ?? {}
      draftState.extraData[id].titleSuffix = titleSuffix
      draftState.extraData[id].value = value
    },
    clear: (draftState) => {
      draftState.ids = []
      draftState.extraData = {}
    },
    isVisibleAlert: (draftState, { payload }) => {
      draftState.showModalAlert = payload.isVisible
      draftState.showModalAlertId = payload.id
    }
  }
})

export default alerts.reducer

const actions = { ...alerts.actions }
export { actions }
