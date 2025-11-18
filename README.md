# Fridge-item-identifier-　loss = criterion(outputs, labels)
　　optimizer.zero_grad()
　　loss.backward()
　　optimizer.step()
　　total_loss += loss.item()
　　print(f"Epoch {epoch+1}: Loss = {total_loss:.4f}")
　　# Save model
　　os.makedirs("../models", exist_ok=True)
　　torch.save(model.state_dict(), SAVE_PATH)
　　print(f"Model saved at: {SAVE_PATH}")
　　if __name__ == "__main__":
　　main()
