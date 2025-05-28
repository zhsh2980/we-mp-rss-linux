#!/bin/bash

# 设置路径变量
DIST_DIR="dist"
TARGET_DIR="../../static"

# 执行构建
npm run build

# 复制文件到static目录
echo "正在复制构建文件到$TARGET_DIR..."
cp -rf $DIST_DIR/* $TARGET_DIR/