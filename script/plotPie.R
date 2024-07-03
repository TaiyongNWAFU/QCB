# 安装并加载必要的包
if (!require("ggplot2")) install.packages("ggplot2", repos='http://cran.us.r-project.org')
library(ggplot2)

# 从命令行参数获取数据
args <- commandArgs(trailingOnly = TRUE)
data1 <- as.numeric(args[1])
data2 <- as.numeric(args[2])
title <- args[3]

# 定义一个函数来绘制单个饼图
plot_pie_chart <- function(data1, data2, title) {
  data <- data.frame(
    category = c("high", "low"),
    value = c(data1, data2)
  )
  
  p <- ggplot(data, aes(x = "", y = value, fill = category)) +
    geom_bar(stat = "identity", width = 1, color = "white", size = 2) +
    coord_polar(theta = "y") +
    theme_void() +
    theme(
      plot.title = element_text(hjust = 0.5, size = 20)
    ) +
    ggtitle(title) +    
	scale_fill_manual(values = c("#1A7CC4", "#41A5EE"))
  
  return(p)
}

# 绘制饼图
p <- plot_pie_chart(data1, data2, title)

# 保存图像为PDF文件
pdf_file <- paste0(title, ".pdf")
pdf(pdf_file, width = 5, height = 5)
print(p)
dev.off()

