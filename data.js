
// Database bài học - Thêm bài mới bằng cách copy và chỉnh sửa
import { a1Data } from './data/a1.js';
import { a2Data } from './data/a2.js';
import { b1Data } from './data/b1.js';
import { b2Data } from './data/b2.js';
import { c1Data } from './data/c1.js';
import { c2Data } from './data/c2.js';

export const LESSON_DATABASE = [
    ...a1Data,
    ...a2Data,
    ...b1Data,
    ...b2Data,
    ...c1Data,
    ...c2Data
];
