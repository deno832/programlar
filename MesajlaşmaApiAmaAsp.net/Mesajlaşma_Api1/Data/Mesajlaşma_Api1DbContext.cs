using Mesajlaşma_Api1.Models.Domain;
using Microsoft.EntityFrameworkCore;

namespace Mesajlaşma_Api1.Data
{
	
	public class Mesajlaşma_Api1DbContext: DbContext
	{
        public Mesajlaşma_Api1DbContext(DbContextOptions dbContextOptions): base(dbContextOptions)
        {
            
        }




		public DbSet<User> Users { get; set; }
        public DbSet<Message> Messages { get; set; }

		protected override void OnModelCreating(ModelBuilder modelBuilder)
		{
			modelBuilder.Entity<Message>()
				.HasOne(m => m.Sender)
				.WithMany()
				.HasForeignKey(m => m.SenderId)
				.OnDelete(DeleteBehavior.Restrict); // Bu satır CASCADE davranışını kaldırır

			modelBuilder.Entity<Message>()
				.HasOne(m => m.Receiver)
				.WithMany()
				.HasForeignKey(m => m.ReceiverId)
				.OnDelete(DeleteBehavior.Restrict); // Bu satır CASCADE davranışını kaldırır
		}
	}

}
