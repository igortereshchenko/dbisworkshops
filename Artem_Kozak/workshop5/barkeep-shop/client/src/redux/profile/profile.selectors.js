import {createSelector} from "reselect";

const selectProfileUpdate = state => state.profile;

export const selectProfileUpdateHidden = createSelector(
    [selectProfileUpdate],
    profile => profile.hidden
);