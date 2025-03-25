# Criação manual do data frame com os dados da imagem
dados <- data.frame(
  Cultura = c("café", "milho", "milho", "café", "milho", "café"),
  Area_m2 = c(10000, 10000, 9604, 17940, 40000, 78200),
  Produto = c("Fosfato", "Calcário", "Calcário", "Fosfato", "Calcário", "Fosfato"),
  Insumo_L = c(5000, 3000, 1470, 8970, 12000, 11615),
  Aplicacao = c("Avião ou Drone", "Trator", "Trator", "Avião ou Drone", "Avião ou Drone", "Trator")
)

# Visualização dos dados
print("📋 Dados das lavouras:")
print(dados)

# Estatísticas - Área
media_area <- mean(dados$Area_m2)
desvio_area <- sd(dados$Area_m2)

# Estatísticas - Insumo
media_insumo <- mean(dados$Insumo_L)
desvio_insumo <- sd(dados$Insumo_L)

# Resultados
cat("\n📊 Estatísticas da Área Plantada:\n")
cat("Média da área:", round(media_area, 2), "m²\n")
cat("Desvio padrão da área:", round(desvio_area, 2), "m²\n")

cat("\n📊 Estatísticas do Insumo Aplicado:\n")
cat("Média do insumo:", round(media_insumo, 2), "L\n")
cat("Desvio padrão do insumo:", round(desvio_insumo, 2), "L\n")

