import {proofRecords} from './fenek-proof-reference';
import {flowRecords} from './fenek-flow-reference';
import {paintRecords} from './fenek-paint-reference';
import type {OtherRecord} from './fenek-other-technical-core';

/** All 34 PROOF / FLOW / PAINT technical sheets, three localized versions each. */
export const otherTechnicalRecords:Record<string,OtherRecord>={
 ...proofRecords,...flowRecords,...paintRecords
};
export const otherTechnicalCodes=Object.keys(otherTechnicalRecords);
